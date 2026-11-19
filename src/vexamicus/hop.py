"""Hop controller over a MotionBus."""

from __future__ import annotations

from vexamicus.motion_bus import MotionBus, SimMotionBus
from vexamicus.types import HopMetrics, MotionState


class HopController:
    """Issues jump requests and collects hop metrics."""

    def __init__(self, bus: MotionBus, *, default_extension: float = 0.8) -> None:
        self.bus = bus
        self.default_extension = default_extension
        self.metrics = HopMetrics()

    def queue_jump(self, *, extension: float | None = None) -> None:
        ext = self.default_extension if extension is None else extension
        self.bus.set_leg_extension(ext)
        if isinstance(self.bus, SimMotionBus):
            self.bus.request_jump()

    def tick(self, dt_s: float = 0.01) -> MotionState:
        state = self.bus.tick(dt_s)
        self.metrics.samples.append(state)
        if state.hop_count > self.metrics.hops:
            self.metrics.hops = state.hop_count
        if state.peak_height_m > self.metrics.peak_height_m:
            self.metrics.peak_height_m = state.peak_height_m
        if state.last_flight_time_s > 0:
            # keep latest flight; sum approximate unique hops via count * last is wrong —
            # store max last flight as representative for phase 0
            self.metrics.total_flight_time_s = max(
                self.metrics.total_flight_time_s, state.last_flight_time_s
            )
        return state

    def run_jumps(self, count: int, *, dt_s: float = 0.01, max_steps: int = 5000) -> HopMetrics:
        """Queue `count` hops sequentially and tick until idle or max_steps."""
        done = 0
        steps = 0
        while done < count and steps < max_steps:
            before = self.bus.read_state().hop_count
            if before <= done:
                self.queue_jump()
            self.tick(dt_s)
            after = self.bus.read_state().hop_count
            if after > done and self.bus.read_state().height_m <= 1e-6:
                done = after
            steps += 1
        return self.metrics

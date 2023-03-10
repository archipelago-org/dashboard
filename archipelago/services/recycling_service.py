from archipelago.models.co2_reduction import Co2Reduction

DUMMY_COLLECTED = 1578
DUMMY_RECYCLED = 1254
DUMMY_ACCUS = DUMMY_COLLECTED + DUMMY_RECYCLED


class RecyclingService:

    def get_co2_reduction(self) -> Co2Reduction:
        response = Co2Reduction(
            sequestration=self._sequestration(DUMMY_COLLECTED),
            abatement=self._abatement(DUMMY_COLLECTED, DUMMY_RECYCLED),
            plastic_collected=DUMMY_COLLECTED,
            plastic_recycled=DUMMY_RECYCLED,
            accus_issued=DUMMY_ACCUS
        )
        return response

    def _sequestration(self, collected: float) -> float:
        # TODO: add actual calculation
        return collected

    def _abatement(self, collected: float, recycled: float) -> float:
        # TODO: add actual calculation
        return collected / 2 + recycled / 10

from archipelago.models.co2 import Co2Response

DUMMY_COLLECTED = 1578
DUMMY_RECYCLED = 1254
DUMMY_ACCUS = DUMMY_COLLECTED + DUMMY_RECYCLED


def get_co2() -> Co2Response:
    response = Co2Response(
        sequestration=sequestration(DUMMY_COLLECTED),
        abatement=abatement(DUMMY_COLLECTED, DUMMY_RECYCLED),
        plastic_collected=DUMMY_COLLECTED,
        plastic_recycled=DUMMY_RECYCLED,
        accus_issued=DUMMY_ACCUS
    )
    return response


def sequestration(collected: float) -> float:
    # TODO: add actual algo
    return collected


def abatement(collected: float, recycled: float) -> float:
    # TODO: add actual algo
    return collected / 2 + recycled / 10

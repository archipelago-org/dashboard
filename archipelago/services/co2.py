from archipelago.models.co2 import Co2Result

DUMMY_COLLECTED = 1578
DUMMY_RECYCLED = 1254


def get_co2():
    result = Co2Result(
        sequestration=sequestration(DUMMY_COLLECTED),
        abatement=abatement(DUMMY_COLLECTED, DUMMY_RECYCLED),
        plastic_collected=DUMMY_COLLECTED,
        plastic_recycled=DUMMY_RECYCLED
    )
    return result


def sequestration(collected: float) -> float:
    # TODO: add actual algo
    return collected


def abatement(collected: float, recycled: float) -> float:
    # TODO: add actual algo
    return collected / 2 + recycled / 10

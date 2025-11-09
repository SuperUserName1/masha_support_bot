from aiogram.fsm.state import State, StatesGroup

class EmotionalState(StatesGroup):
    emotional = State()
    description = State()

class SelfCareState(StatesGroup):
    pass
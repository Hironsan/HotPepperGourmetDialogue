# -*- coding: utf-8 -*-
from modules.DialogueManagement.manager import DialogueManager
from modules.DialogueManagement.state import DialogueState
from modules.LanguageGeneration.generator import LanguageGenerator
from modules.LanguageUnderstanding.DialogueActType.predictor import DialogueActTypePredictor
from modules.LanguageUnderstanding.NamedEntityExtraction.extractor import NamedEntityExtractor
from modules.BackEnd.APIs.hotpepper import HotPepperGourmetAPI

if __name__ == '__main__':
    generator = LanguageGenerator()
    predictor = DialogueActTypePredictor()
    extractor = NamedEntityExtractor()
    state = DialogueState()
    manager = DialogueManager()
    api = HotPepperGourmetAPI()

    while True:
        # Input from User
        sent = input()

        # Language Understanding
        user_act_type = predictor.predict(sent)
        named_entities = extractor.extract(sent)

        # Update Dialogue state
        manager.update_dialogue_state(user_act_type, named_entities, state)
        sys_act_type = manager.select_action(state, api)

        # Generate Sentence
        sent = generator.generate_sentence(sys_act_type)
        print(sent)
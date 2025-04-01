from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFornecerSuporte(Action):
    def name(self) -> Text:
        return "action_fornecer_suporte"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        problema = tracker.get_slot("problema")
        solucao = self.buscar_solucao(problema)

        if solucao:
            dispatcher.utter_message(text=solucao)
        else:
            dispatcher.utter_message(text="Vou transferir você para um atendente humano. Aguarde um momento...")
        
        return []

    def buscar_solucao(self, problema: Text) -> Text:
        # Simulação de base de dados de soluções
        base_solucoes = {
            "acesso": "Siga estas etapas: 1. Clique em 'Esqueci a senha'. 2. Verifique seu e-mail para redefinir.",
            "plano": "Planos disponíveis: Básico (R$20/mês), Premium (R$35/mês). Acesse [configurações da conta] para alterar.",
            "tecnico": "Solução técnica: Reinicie o aplicativo. Se persistir, atualize para a versão mais recente."
        }
        return base_solucoes.get(problema.lower(), "")
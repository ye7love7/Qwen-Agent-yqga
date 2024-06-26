from typing import Iterator, List

from qwen_agent.agents.assistant import Assistant
from qwen_agent.llm.schema import Message
from qwen_agent.settings import DEFAULT_MAX_REF_TOKEN

PENDING_USER_INPUT = '<!-- INTERRUPT: PENDING_USER_INPUT -->'


class UserAgent(Assistant):

    def _run(self,
             messages: List[Message],
             lang: str = 'en',
             max_ref_token: int = DEFAULT_MAX_REF_TOKEN,
             **kwargs) -> Iterator[List[Message]]:

        yield [Message(role='user', content=PENDING_USER_INPUT, name=self.name)]

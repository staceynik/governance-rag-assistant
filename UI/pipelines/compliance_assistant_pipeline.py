"""
Open WebUI Pipeline: Compliance Assistant

Simple pipeline stub used for integration testing.
Returns a fixed response for any user message.
"""

from typing import List, Optional, Dict, Any

class Pipeline:
    name = "Compliance Assistant"
    id = "compliance_assistant_pipeline"

    version = "0.1.0"
    description = "Pipeline stub returning a fixed response for testing purposes."

    async def on_startup(self):
        print("[compliance_assistant_pipeline] startup")

    async def on_shutdown(self):
        print("[compliance_assistant_pipeline] shutdown")

    def pipe(
        self,
        user_message: str,
        model_id: str,
        messages: List[Dict[str, Any]],
        body: Dict[str, Any],
        __user__: Optional[Dict[str, Any]] = None,
        __event_emitter__=None,
        **kwargs, 
    ):
       
        user_msg = ""
        try:
            msgs = body.get("messages", [])
            if msgs:
                user_msg = msgs[-1].get("content", "")
        except Exception:
            pass
        print(f"[compliance_assistant_pipeline] user message: {user_msg!r}")

        # Option 1: simple non-streaming response
        return "Compliance Assistant pipeline is running."

        # Option 2: streaming response example
        # if __event_emitter__:
        #     await __event_emitter__({
        #         "type": "message",
        #         "data": {"content": "Compliance Assistant pipeline is running."}
        #     })
        # return ""
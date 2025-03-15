from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class SimpleJinaTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        url = tool_parameters.get["url"]
        try:
            response = requests.get(url)
            response.raise_for_status()
            yield self.create_json_message({
                "result": response.text
            })
        except requests.exceptions.RequestException as e:
            yield self.create_json_message({
                "error": f"An error occurred: {str(e)}"
            })

"""API client management for the Codegen MCP server."""

import os

from codegen.cli.api.client import RestAPI
from codegen.cli.api.endpoints import API_ENDPOINT

# Global API client instance
_api_client = None


def get_api_client():
    """Get or create the API client instance."""
    global _api_client

    if _api_client is None:
        # Get API key from environment
        api_key = os.getenv("CODEGEN_API_KEY")
        if not api_key:
            msg = "CODEGEN_API_KEY environment variable is required"
            raise RuntimeError(msg)

        # Create the API client
        _api_client = RestAPI(auth_token=api_key)

    return _api_client


def is_api_client_available() -> bool:
    """Check if the API client is available."""
    return True

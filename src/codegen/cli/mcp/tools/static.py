"""Static Codegen API tools for the MCP server."""

import json
from typing import Annotated

from fastmcp import Context, FastMCP

from ..api_client import get_api_client
from codegen.cli.api.endpoints import API_ENDPOINT


def register_static_tools(mcp: FastMCP):
    """Register static Codegen API tools with the MCP server."""

    @mcp.tool()
    def create_agent_run(
        prompt: Annotated[str, "The prompt/task for the agent to execute"],
        repo_name: Annotated[str | None, "Repository name (optional)"] = None,
        branch_name: Annotated[str | None, "Branch name (optional)"] = None,
        ctx: Context | None = None,
    ) -> str:
        """Create a new agent run in the configured organization."""
        try:
            api_client = get_api_client()

            # Prepare the request data
            data = {"prompt": prompt}
            if repo_name:
                data["repo_name"] = repo_name
            if branch_name:
                data["branch_name"] = branch_name

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/agent/run"
            response = api_client._session.post(endpoint, json=data, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error creating agent run: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error creating agent run: {e}"

    @mcp.tool()
    def get_agent_run(
        agent_run_id: Annotated[int, "Agent run ID"],
        ctx: Context | None = None,
    ) -> str:
        """Get details of a specific agent run."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/agent/run/{agent_run_id}"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error getting agent run: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error getting agent run: {e}"

    @mcp.tool()
    def get_organizations(
        ctx: Context | None = None,
    ) -> str:
        """Get list of organizations the user has access to."""
        try:
            api_client = get_api_client()

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error getting organizations: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error getting organizations: {e}"

    @mcp.tool()
    def get_users(
        ctx: Context | None = None,
    ) -> str:
        """Get list of users in the configured organization."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/users"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error getting users: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error getting users: {e}"

    @mcp.tool()
    def get_user(
        user_id: Annotated[int, "User ID"],
        ctx: Context | None = None,
    ) -> str:
        """Get details of a specific user in the configured organization."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/users/{user_id}"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error getting user: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error getting user: {e}"

    @mcp.tool()
    def list_agent_runs(
        ctx: Context | None = None,
    ) -> str:
        """List all agent runs in the configured organization."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/agent/runs"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error listing agent runs: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error listing agent runs: {e}"

    @mcp.tool()
    def resume_agent_run(
        agent_run_id: Annotated[int, "Agent run ID to resume"],
        prompt: Annotated[str, "Additional prompt/instructions for the resumed run"],
        ctx: Context | None = None,
    ) -> str:
        """Resume a paused or completed agent run with additional instructions."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/agent/run/resume"
            data = {"agent_run_id": agent_run_id, "prompt": prompt}
            response = api_client._session.post(endpoint, json=data, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error resuming agent run: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error resuming agent run: {e}"

    @mcp.tool()
    def get_repositories(
        ctx: Context | None = None,
    ) -> str:
        """Get list of repositories in the configured organization."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/repositories"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error getting repositories: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error getting repositories: {e}"

    @mcp.tool()
    def get_pull_requests(
        ctx: Context | None = None,
    ) -> str:
        """Get list of pull requests in the configured organization."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/pull-requests"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error getting pull requests: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error getting pull requests: {e}"

    @mcp.tool()
    def get_integrations(
        ctx: Context | None = None,
    ) -> str:
        """Get list of integrations in the configured organization."""
        try:
            api_client = get_api_client()

            # Get org_id from environment
            import os
            org_id = os.getenv("CODEGEN_ORG_ID")
            if not org_id:
                return "Error: CODEGEN_ORG_ID environment variable is required"

            # Make the API call
            endpoint = f"{API_ENDPOINT}/v1/organizations/{org_id}/integrations"
            response = api_client._session.get(endpoint, headers=api_client._get_headers())

            if response.status_code == 200:
                result = response.json()
                return json.dumps(result, indent=2)
            else:
                return f"Error getting integrations: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error getting integrations: {e}"

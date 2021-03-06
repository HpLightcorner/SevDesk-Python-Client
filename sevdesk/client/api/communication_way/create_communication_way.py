from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.communication_way_model import CommunicationWayModel
from ...models.create_communication_way_response_201 import (
    CreateCommunicationWayResponse201,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CommunicationWayModel,
) -> Dict[str, Any]:
    url = "{}/CommunicationWay".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, CreateCommunicationWayResponse201]]:
    if response.status_code == 201:
        response_201 = CreateCommunicationWayResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, CreateCommunicationWayResponse201]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CommunicationWayModel,
) -> Response[Union[Any, CreateCommunicationWayResponse201]]:
    """Create a new contact communication way

     Creates a new contact communication way.

    Args:
        json_body (CommunicationWayModel): Contact communication way model

    Returns:
        Response[Union[Any, CreateCommunicationWayResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CommunicationWayModel,
) -> Optional[Union[Any, CreateCommunicationWayResponse201]]:
    """Create a new contact communication way

     Creates a new contact communication way.

    Args:
        json_body (CommunicationWayModel): Contact communication way model

    Returns:
        Response[Union[Any, CreateCommunicationWayResponse201]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CommunicationWayModel,
) -> Response[Union[Any, CreateCommunicationWayResponse201]]:
    """Create a new contact communication way

     Creates a new contact communication way.

    Args:
        json_body (CommunicationWayModel): Contact communication way model

    Returns:
        Response[Union[Any, CreateCommunicationWayResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CommunicationWayModel,
) -> Optional[Union[Any, CreateCommunicationWayResponse201]]:
    """Create a new contact communication way

     Creates a new contact communication way.

    Args:
        json_body (CommunicationWayModel): Contact communication way model

    Returns:
        Response[Union[Any, CreateCommunicationWayResponse201]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

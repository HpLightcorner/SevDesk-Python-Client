from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contact_get_communication_ways_response_200 import (
    ContactGetCommunicationWaysResponse200,
)
from ...types import Response


def _get_kwargs(
    contact_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/Contact/{contactId}/getCommunicationWays".format(
        client.base_url, contactId=contact_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ContactGetCommunicationWaysResponse200]]:
    if response.status_code == 200:
        response_200 = ContactGetCommunicationWaysResponse200.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, ContactGetCommunicationWaysResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    contact_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ContactGetCommunicationWaysResponse200]]:
    """Get communication ways of contact

     Returns all communication ways of a given contact.

    Args:
        contact_id (int):

    Returns:
        Response[Union[Any, ContactGetCommunicationWaysResponse200]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    contact_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ContactGetCommunicationWaysResponse200]]:
    """Get communication ways of contact

     Returns all communication ways of a given contact.

    Args:
        contact_id (int):

    Returns:
        Response[Union[Any, ContactGetCommunicationWaysResponse200]]
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    contact_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ContactGetCommunicationWaysResponse200]]:
    """Get communication ways of contact

     Returns all communication ways of a given contact.

    Args:
        contact_id (int):

    Returns:
        Response[Union[Any, ContactGetCommunicationWaysResponse200]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    contact_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ContactGetCommunicationWaysResponse200]]:
    """Get communication ways of contact

     Returns all communication ways of a given contact.

    Args:
        contact_id (int):

    Returns:
        Response[Union[Any, ContactGetCommunicationWaysResponse200]]
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
        )
    ).parsed
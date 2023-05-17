# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
import json

class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    **kwargs,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    json_output = kwargs.get("json", False)

    root = ET.fromstring(xml)

    # parsing channel data
    channel_dict = {}
    for child in root.findall('./channel/*'):
        if child.tag == 'category':
            channel_dict.setdefault('Categories', []).append(child.text)
        else:
            channel_dict[child.tag] = child.text

    # parsing item data
    items_list = []
    for item in root.findall('./channel/item')[:limit]:
        item_dict = {}
        for child in item:
            if child.tag == 'category':
                item_dict.setdefault('Categories', []).append(child.text)
            else:
                item_dict[child.tag] = child.text
        items_list.append(item_dict)

    # format output
    output = []
    if not json_output:
        # format output as plain text
        for key, value in channel_dict.items():
            if key == 'Categories':
                output.append(f"{key}: {', '.join(value)}")
            else:
                output.append(f"{key}: {value}")

        for item in items_list:
            item_str = []
            for key, value in item.items():
                if key == 'Categories':
                    item_str.append(f"{key}: {', '.join(value)}")
                else:
                    item_str.append(f"{key}: {value}")
            output.append('\n'.join(item_str))
    else:
        # format output as json
        output_dict = {}
        for key, value in channel_dict.items():
            output_dict[key] = value
        output_dict['items'] = items_list
        output.append(json.dumps(output_dict, indent=4))

    return output

def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()

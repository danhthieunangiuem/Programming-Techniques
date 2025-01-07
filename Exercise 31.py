def parse_url(url: str) -> dict:
    """Parse a URL into components: protocol, hostname, domain, directory, filename, query parameters."""

    result = {
        "protocol": "",
        "hostname": "",
        "domain": "",
        "directory": "",
        "filename": "",
        "query_parameters": ""
    }

    # Split protocol
    if "://" in url:
        result["protocol"], url = url.split("://", 1)

    # Split query parameters
    if "?" in url:
        url, result["query_parameters"] = url.split("?", 1)

    # Extract hostname and directory
    if "/" in url:
        hostname_and_domain, *directories = url.split("/", 1)
        result["hostname"] = hostname_and_domain
        if "." in hostname_and_domain:
            result["domain"] = ".".join(hostname_and_domain.split(".")[-2:])
        if directories:
            directory_path = directories[0]
            if "/" in directory_path:
                *dirs, filename = directory_path.rsplit("/", 1)
                result["directory"] = "/".join(dirs)
                result["filename"] = filename
            else:
                result["filename"] = directory_path
    else:
        result["hostname"] = url
        if "." in url:
            result["domain"] = ".".join(url.split(".")[-2:])

    return result

url_input = input("Enter a URL: ").strip()
components = parse_url(url_input)

for key, value in components.items():
    print(f"{key.capitalize()}: {value}")
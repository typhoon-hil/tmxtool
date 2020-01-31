from error_manager import WARNING_CODE_INVALID_FORMAT, run_warning


def create_dicts(lines):
    ret = {}

    idx = 0
    while idx < len(lines):
        if lines[idx].strip() == '':
            idx += 1
            continue

        id = lines[idx].strip()
        idx += 1

        timestamp = lines[idx].strip()
        idx += 1

        content = ""
        while len(lines) > idx and lines[idx].strip() != '\n':
            content += lines[idx].strip()
            idx += 1

        if id.strip() == '' or timestamp.strip() == '' or content.strip() == '':
            run_warning(WARNING_CODE_INVALID_FORMAT, [id, timestamp, content])
            continue

        ret[timestamp] = (id, content)
        idx += 1

    return ret

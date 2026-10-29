def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["message"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"path": file_path, "status": "passed" if len(errors) == 0 else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "code": error["code"],
            "filename": error["filename"],
            "line_number": error["line_number"],
            "column_number": error["column_number"],
            "text": error["text"],
            "physical_line": error["physical_line"],
        }
        for data in linter_report.values()
        if data.get("status") == "failed"
        for error in data.get("message", [])
    ]

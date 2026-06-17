# -*- coding: utf-8 -*-
import os
from typing import Any, cast

env = cast(Any, globals().get("env"))

if env is None:
    raise RuntimeError(
        "This script must be executed inside Odoo shell. "
        "Do not run it with plain Python."
    )

public_url = os.getenv("ODOO_PUBLIC_URL")

if not public_url:
    raise ValueError("Missing ODOO_PUBLIC_URL environment variable")

public_url = public_url.rstrip("/")

params = env["ir.config_parameter"].sudo()
params.set_param("web.base.url", public_url)
params.set_param("web.base.url.freeze", "True")

env.cr.commit()

print("Odoo base URL updated successfully.")
print(f"web.base.url = {public_url}")
print("web.base.url.freeze = True")

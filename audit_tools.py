import os
import re

tools = [
    (
        "cursor_tamper_proxy.py",
        os.path.expandvars(r"%LOCALAPPDATA%\SusuAIOverclock-cache\1.5.7-electron44.4.3\resources\packs\cursor\materials\tools\cursor_tamper_proxy.py")
    ),
    (
        "xg_elf_tool.py",
        os.path.expandvars(r"%LOCALAPPDATA%\SusuAIOverclock-cache\1.5.7-electron44.4.3\resources\packs\codex\materials\skills\elf-local-auth-patcher\scripts\xg_elf_tool.py")
    ),
    (
        "linker_static_unwrap.py",
        os.path.expandvars(r"%LOCALAPPDATA%\SusuAIOverclock-cache\1.5.7-electron44.4.3\resources\packs\codex\materials\skills\linker-fake-load-unwrapper\scripts\linker_static_unwrap.py")
    ),
    (
        "shiyi_assembler.py",
        os.path.expandvars(r"%LOCALAPPDATA%\SusuAIOverclock-cache\1.5.7-electron44.4.3\resources\packs\codex\materials\tools\shiyi_assembler.py")
    ),
    (
        "codex-instruct.py",
        os.path.expandvars(r"%LOCALAPPDATA%\SusuAIOverclock-cache\1.5.7-electron44.4.3\resources\packs\codex\materials\skills\zzy-codex5.6\zzy-Codex-5.6\codex-instruct.py")
    )
]

for name, path in tools:
    print(f"==================================================")
    print(f"Auditing: {name}")
    print(f"Path: {path}")
    if not os.path.exists(path):
        print("  -> File not found!")
        continue
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
    except Exception as e:
        print(f"  -> Failed to read file: {e}")
        continue
    
    print(f"  Length: {len(code)} characters ({len(code.splitlines())} lines)")
    
    # 1. 外部网络连接 (URLs & IP)
    urls = set(re.findall(r'https?://[^\s\'\"\<\>]+', code))
    print(f"  URLs: {len(urls)}")
    for u in sorted(urls)[:10]:
        print(f"    - {u}")
    
    # 2. 危险调用
    for kw in ['requests.', 'urllib.', 'socket.', 'os.system', 'subprocess.Popen', 'subprocess.run', 'eval(', 'exec(', 'connect(', 'sendto(']:
        cnt = code.count(kw)
        if cnt > 0:
            print(f"  Dangerous Call: {kw} -> {cnt} times")

    # 3. 环境变量与敏感凭据嗅探
    env_matches = re.findall(r'os\.environ\.get\([\'\"][^\'\"]+[\'\"]\)|process\.env\.[A-Za-z0-9_]+', code)
    if env_matches:
        print(f"  Env Reads: {set(env_matches)}")


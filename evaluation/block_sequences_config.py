"""
Block sequences configuration for nodes A through H (Rows 1 to 80).
"""

BLOCK_SEQUENCES = {
    "A": [
        # 1-10
        "none", "none", "none", "none", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 11-20
        "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 21-30
        "syn-flood", "none", "none", "none", "none", "none", "none", "none", "none", "none",
        # 31-40
        "none", "none", "none", "none", "none", "none", "none", "none", "none", "none",
        # 41-50
        "none", "none", "none", "none", "none", "none", "none", "Backdoor", "Backdoor", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "none", "none",
        # 71-80
        "none", "none", "none", "none", "none", "none", "none", "none", "none", "none",
    ],
    "B": [
        # 1-10
        "none", "none", "none", "none", "none", "none", "none", "none", "none", "none",
        # 11-20
        "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 21-30
        "syn-flood", "none", "none", "none", "none", "none", "none", "none", "none", "none",
        # 31-40
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "none", "none", "none", "none", "none",
        # 41-50
        "none", "none", "none", "none", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "none", "none",
        # 71-80
        "none", "none", "none", "none", "none", "noneX2", "noneX2", "noneX2", "noneX2", "noneX2",
    ],
    "C": [
        # 1-10
        "none", "none", "none", "none", "none", "none", "none", "none", "none", "none",
        # 11-20
        "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 21-30
        "syn-flood", "none", "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood",
        # 31-40
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "none", "none", "none", "none", "none",
        # 41-50
        "none", "none", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "none", "none",
        # 71-80
        "none", "none", "none", "none", "none", "noneX2", "noneX2", "noneX2", "noneX2", "noneX2",
    ],
    "D": [
        # 1-10
        "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 11-20
        "none", "none", "none", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 21-30
        "Backdoor", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 31-40
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "none", "none", "none", "none", "none",
        # 41-50
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "none", "none",
        # 71-80
        "none", "none", "none", "none", "none", "noneX2", "noneX2", "noneX2", "noneX2", "noneX2",
    ],
    "E": [
        # 1-10
        "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 11-20
        "none", "none", "none", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 21-30
        "Backdoor", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 31-40
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "none", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 41-50
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood",
        # 71-80
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "noneX2", "noneX2", "noneX2", "noneX2", "noneX2",
    ],
    "F": [
        # 1-10
        "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 11-20
        "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 21-30
        "syn-flood", "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 31-40
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "none", "none", "Backdoor", "Backdoor", "Backdoor",
        # 41-50
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood",
        # 71-80
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "noneX2", "noneX2", "noneX2", "noneX2", "noneX2",
    ],
    "G": [
        # 1-10
        "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 11-20
        "none", "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 21-30
        "syn-flood", "none", "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 31-40
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "none", "none", "none", "none", "Backdoor",
        # 41-50
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood",
        # 71-80
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "noneX2", "noneX2", "noneX2", "noneX2", "noneX2",
    ],
    "H": [
        # 1-10
        "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 11-20
        "none", "none", "none", "none", "none", "none", "none", "none", "none", "none",
        # 21-30
        "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood", "syn-flood", "syn-flood",
        # 31-40
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "none", "none", "none", "none", "none",
        # 41-50
        "none", "none", "none", "none", "none", "none", "none", "none", "none", "Backdoor",
        # 51-60
        "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "Backdoor", "none", "none", "none",
        # 61-70
        "none", "none", "none", "none", "none", "none", "none", "none", "syn-flood", "syn-flood",
        # 71-80
        "syn-flood", "syn-flood", "syn-flood", "none", "none", "noneX2", "noneX2", "noneX2", "noneX2", "noneX2",
    ],
}
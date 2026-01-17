from pathlib import Path

def load_config(path: str) -> dict:
    cfg = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        k, v = line.split(":", 1)
        cfg[k.strip()] = v.strip()
    return cfg

def main():
    cfg_path = "configs/default.yml"
    cfg = load_config(cfg_path)

    print("running backtest")
    print(f"config: {cfg_path}")
    print(f"strategy: {cfg.get('strategy')}")
    print(f"universe: {cfg.get('universe')}")
    print(f"dates: {cfg.get('start')} -> {cfg.get('end')}")
    print(f"lookback_days: {cfg.get('lookback_days')}")
    print(f"rebalance: {cfg.get('rebalance')}")
    print(f"initial_cash: {cfg.get('initial_cash')}")
    print("status: OK (engine stub)")

if __name__ == "__main__":
    main()

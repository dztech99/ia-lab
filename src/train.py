import yaml
from llama_factory import Trainer

def main():
    cfg = yaml.safe_load(open("config/config.yaml"))
    trainer = Trainer(cfg)
    trainer.train()

if __name__ == "__main__":
    main()

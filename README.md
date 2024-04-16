# AI-Image-Generation-Orchestrator
AI Image Generation Orchestrator - provides one CLI interface for local Stable Defusion (Automatic1111 API) and PixAI image generation (For Rimworld mod [rimworld-avatar](https://github.com/bolphen/rimworld-avatar)).

## Acknowledgement:
* [PixAI (Core Project)](https://github.com/shidktbw/pixaiAPI) and [Rimworld Specific](https://github.com/bolphen/pixaiAPI)
* [Stable Defusion](https://gist.github.com/w-e-w/0f37c04c18e14e4ee1482df5c4eb9f53)

## Use example:
```bash
python orchestrator.py sdlocal "girl, cowboy hat, mask, armor" ./refimg.png
```
or
```bash
python orchestrator.py pixai "girl, cowboy hat, mask, armor" ./refimg.png
```

***sdlocal/pixai*** - service to use

***"girl, cowboy hat, mask, armor"*** - prompt

***./refimg.png*** - reference image for generation

## Setup:

1. StableDefusion(Automatic1111):
    - in `StableDefusion/configuration.py` you can configure basic exposed settings
    - if you want more control you can edit payload in `StableDefusion/payload.py`
2. PixAI:
    - configure your API tocken in `PixAI/credentials.py`
    - and see `PixAI/repaint.py`

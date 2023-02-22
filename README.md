# Art (Artist reference tool)

## A tool for artist

### Goals 
- Store references
- Display references
- Handle timed drawing session

### TODO
- Tool to save / tag references (cli)
- Adapters for storage / tagging (only local disk first)
- Web app to display references / search by tags (react)


### Building and running Art CLI

```bash
docker build -t art_image . --rm
MSYS_NO_PATHCONV=1 docker run -it --name art -v "$(pwd)/data:/home/root/data" --rm art_image <url>
```

or use

```
    run.sh <url>
```

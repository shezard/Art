import cli

def main():
    [url, extension] = cli.parse_arguments()
    [file_name, md5hash, content] = cli.fetch_image(url, extension)
    cli.save_image(file_name, content)
    cli.display_image(file_name)
    tags = cli.get_tags()
    cli.save_tags(md5hash, tags)

if __name__ == '__main__':
    main()
docker run -it -v "$(pwd)":/srv/files/ --env COMMAND_LINE="-f data/src-test.500 -t data/translated.txt -m eng-cat" --rm jordimash/use-models-tools --name jordimash/use-models-tools

from fast_autocomplete import autocomplete_factory

content_files = {
    'words': {
        'filepath': 'count.json',
        'compress': True  # means compress the graph data in memory
    }
}

autocomplete = autocomplete_factory(content_files=content_files)

def wpredict(inp,x):
    return(autocomplete.search(word=inp,size=x))

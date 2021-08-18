# CSVs and Pickling

Python has builtin csv module to read/write csvs

## Reading from csv files

`reader` - lets you iterate over rows of the CSV as a list, each line is a list.
  - basic iterator, only allows you to iterate through once.
  - The header line is outputted in the same way as the rest of the file.
    - Can use `next()` to skip the header (first line) if not needed

`DictReader` - lets you iterate over rows of the CSV as OrderedDict
  - The keys are set automatically to the same as the headers

Readers accept a delimeter kwarg in case your data isnt separated by commas `,`.

## Wrting to csv files

`writer` - creates a writer object for writing to csv


## Pickling

The `pickle` module is used to serialize and de-serialize a python object structure.
`pickling` is the process to convert into a byte stream, `unpickling` is the inverse.
- basically can save the current status of something to use later.
- Data is not readable when pickled.

```
# To pickle an object:
with open("pets.pickle", "wb") as file:
	pickle.dump(blue, file)
```

## Json pickling
You can use `jsonpickle`, python library similar to pickle, that works with json.
- Have to install via pip.

```
# json.dumps returns a JSON STRING:

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# results in '["foo", {"bar": ["baz", null, 1.0, 2]}]'
```

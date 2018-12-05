# geoschool
Address verification for UCS to send decals

preclean.py does some basic address parsing and verification. If smartystreets credits are short, run preclean.py and only send valid addresses to smartystreets. Otherwise, smartystreets does an equally if not better job at parsing address components, so recommend dumping raw addresses directly to smartystreets if credits are not a concern.

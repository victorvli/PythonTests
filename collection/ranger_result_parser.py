if __name__ == '__main__':
    inputs = ['*', 'ids, ods, dwd, dws, hds, ads', 'information_schema', 'information, information_schema',
              'information', 'ods', 'ods, ads, dws']
    results = []
    for e in inputs:
        elements = e.split(', ')
        results.extend(elements)
    results = set(results)
    if '*' in results:
        results = ['*']
    print(results)

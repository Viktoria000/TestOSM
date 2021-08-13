direct_param_list_value = [
    {
        "req_params": {"city": "moskow"},
        "expected_lat": "55.7504461",
        "expected_lon": "37.6174943"
    },
    {
        "req_params": {"q": "Ялта"},
        "expected_lat": "44.4970713",
        "expected_lon": "34.1586871"
    },
    {
        "req_params": {"city": "Kazan"},
        "expected_lat": "55.7823540",
        "expected_lon": "49.1242260"
    },
    {
        "req_params": {"street": "некорректные_параметры"},
        "expected_lat": "43.2611844",
        "expected_lon": "-73.5800934"
    }
    # { Для данного набора возвращаются всегда разные координаты)
    #     "req_params": {"street": "22 Broadway"},
    #     "expected_lat": "40.8921337",
    #     "expected_lon": "-71.312842"
    # }
]



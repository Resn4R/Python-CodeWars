def stringCalculator (numbers: str) -> int:
    return sum(
        list(
            map(int, list( 
                    filter(None, numbers.split(','))
                    )
                )
           )
        )
def _calculate_non_zero_ratios(numbers: list[int | float]) -> list[float]:
    """
    Sıfır olmayan değerlerin oranlarını hesapla.
    
    Args:
        numbers: Sayısal değerler listesi
        
    Returns:
        Sıfır olmayan her değer için 100/değer oranları
    """
    return [100 / num for num in numbers if num != 0]


def average_ratios(numbers: list[int | float]) -> float:
    """
    Sıfır olmayan değerlerin oranlarının ortalamasını hesapla.
    
    Args:
        numbers: Sayısal değerler listesi
        
    Returns:
        Sıfır olmayan değerlerin oranlarının ortalaması.
        Tüm değerler sıfır ise 0 döndür.
    """
    ratios = _calculate_non_zero_ratios(numbers)
    
    if not ratios:
        return 0
    
    return sum(ratios) / len(ratios)


if __name__ == "__main__":
    result = average_ratios([10, 5, 0])
    print(result)

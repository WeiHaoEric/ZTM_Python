def test(num:float, txt:str):
    print(f"call testing! num:{num}, txt:{txt}")
    return True


if __name__== "__main__":
  print("run testing...")
  name = "Eric"
  print(f'{name}')
  test(20, "okla")
  
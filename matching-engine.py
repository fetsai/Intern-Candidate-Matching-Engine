class Order:
    def __init__(self, tipo, side, price, qty):
        self.tipo = tipo
        self.side = side
        self.price = price
        self.qty = qty

class Trade:
    def __init__(self,price, qty):
        self.price = price
        self.qty = qty

def DeleteOrders(listOrder,listIndex):
  # Funcao para deletar as order que foram zeradas da lista
  if len(listIndex) > 0 :
    for i in range(len(listIndex)-1,-1.-1):
      del listOrder[listIndex[i]]
  return listOrder


def MatchingEngine(newOrder,listOrders):
  #Funcao que realiza o matching

  trade = Trade(0,0)
  deleteIndices = []
  
  #######################################
  ### market orders
  if newOrder.tipo == "market":
    indice = 0
    melhorPreco = -1
    # Acha o melhor preco
    for i in range(len(listOrders)):
        if newOrder.side != listOrders[i].side:

          ##### market buy
          if newOrder.side == "buy":
            if melhorPreco < 0 or (listOrders[i].price < melhorPreco and listOrders[i].price > 0):
              indice = i
              melhorPreco = listOrders[i].price

          ##### market sell
          else:
            if listOrders[i].price > melhorPreco:
              indice = i
              melhorPreco = listOrders[i].price

    # Realiza a troca
    if melhorPreco != -1:
      trade.price = melhorPreco
      difQnt = newOrder.qty - listOrders[indice].qty

      # Sobrou qty na ordem
      if difQnt >= 0:
        trade.qty = listOrders[indice].qty
        newOrder.qty = difQnt
        del listOrders[indice]

        # Procura nas proximas orders
        for i in range(len(listOrders)):
          if newOrder.side != listOrders[i].side:
          
            if trade.price == listOrders[i].price:
              difQnt = newOrder.qty - listOrders[i].qty

              if difQnt >= 0:
                trade.qty += listOrders[i].qty
                newOrder.qty = difQnt
                deleteIndices.append(i)
              else:
                trade.qty += newOrder.qty
                listOrders[i].qty = -difQnt
                newOrder.qty = 0
        listOrders = DeleteOrders(listOrders,deleteIndices)

      else:
        trade.qty = newOrder.qty
        listOrders[indice].qty = -difQnt
        newOrder.qty = 0

  #######################################
  ### limit orders
  else:
    trade.price = newOrder.price
    for i in range(len(listOrders)):
      if newOrder.side != listOrders[i].side:
        if newOrder.price == listOrders[i].price or listOrders[i].price == -1:
          difQnt = newOrder.qty - listOrders[i].qty

          if difQnt >= 0:
            trade.qty += listOrders[i].qty
            newOrder.qty = difQnt
            deleteIndices.append(i)
          else:
            trade.qty += newOrder.qty
            listOrders[i].qty = -difQnt
            newOrder.qty = 0
            break          
    listOrders = DeleteOrders(listOrders,deleteIndices)


  return listOrders, newOrder, trade
  

def Main():
      
  listOrders = []
  while(1):
    # Recebe order
    param = str(input()).split()
    # Verifica e cria a order
    try:
      if param[0] == "limit":
        newOrder = Order(param[0], param[1], int(param[2]), int(param[3]))
      elif param[0] == "market":
        newOrder = Order(param[0], param[1], -1, int(param[2]))
      elif param[0] == "stop":
        break
      else:
        print("Formato incorreto de order.")
        continue
      if param[1] != "buy" and param[1] != "sell":
        print("Formato incorreto de order.")
        continue
    except:
      print("Formato incorreto de order.")
      continue

    while(1):
      # Realiza o matching
      listOrders, newOrder, trade = MatchingEngine(newOrder, listOrders)
      
      # Caso de market continua até acabar a qty da ordem ou não ter mais matching
      if trade.qty > 0:
        print("Trade, price: {}, qty: {}".format(trade.price,trade.qty))
        if newOrder.qty != 0:
          if newOrder.tipo == "limit":
            listOrders.append(newOrder)
            break
        else:
          break
      else:
        if newOrder.qty != 0:
          listOrders.append(newOrder)
        break
      



if __name__ == "__main__":
  Main()

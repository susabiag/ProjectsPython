library(EnvStats)
#Lab 3
#r =  revenue
#r = 18

#c = cost
#c = 12

#s = salvage value 50% discounted and eventually sold = 9
#s = 9


#d = units demanded (not controllable, random?)
#demand.dist = c(42,45,40,46,43,44,47,41,51,48)

#q = quantity purchased (decision)
#In the past 40


#Notice that we cannot sell more than the minimum of actual demand and the amount purchased.
#Notice that we cannot sell more than the minimum of actual demand and the amount purchased. Thus, the quantity sold
#at the regular price is the minimum of
#EX: kind of--> units.sold = min(demand,prod.level)

#net profit = rmin(q,d) +smax(0,q−d)−cq



#Problem 1: a. A distribution of the above data (what is the probability of obtaining any given value from the data above?).
#The probability of obtaining any given value from the above data would be 1/20 or 5%, but this is not true because the 
#numbers repeat themselves inside the data.
#The probability of obtaining demand 42 from the above data is: .15%
#The probability of obtaining demand 45 from the above data is: .15%
#The probability of obtaining demand 40 from the above data is: .05%
#The probability of obtaining demand 46 from the above data is: .1%
#The probability of obtaining demand 43 from the above data is: .2%
#The probability of obtaining demand 44 from the above data is: .1%
#The probability of obtaining demand 47 from the above data is: .05%
#The probability of obtaining demand 41 from the above data is: .1%
#The probability of obtaining demand 51 from the above data is: .05%
#The probability of obtaining demand 48 from the above data is: .05%


#Problem 2: b. A random draw from the distribution in part (a).
#demand.dist = c(42,45,40,46,43,44,47,41,51,48)
#demand.prob = c(.15,.15,.05,.1,.2,.1,.05,.1,.05,.05)
#demand = sample(demand.dist,1,prob = demand.prob)

#c. A calculation of the net profit using a choice of q.
#net_profit = (r*min(q,demand)) + (s*max(0,q-demand)) - (c*q)

#d. A loop which executes steps (b)-(c) 1000 times and records the average net profit each time.
demand.dist = c(42, 45, 40, 46, 43, 44, 47, 41, 51, 48)
demand.prob = c(0.15, 0.15, 0.05, 0.1, 0.2, 0.1, 0.05, 0.1, 0.05, 0.05)

# Parameters now in code
r = 18
c = 12
s = 9
nreps = 1000
quantity = c(40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50)  

#Store mean profit for each q
mean_profits = vector('numeric', length(quantity))  

# Initialize profit distribution
profit.dist = vector(mode = 'numeric', length = nreps)

# Loop over different quantities
for (i in 1:length(quantity)) {
  q = quantity[i]
  
  for (j in 1:nreps) {
    demand = sample(demand.dist, 1, prob = demand.prob)
    
    # Calculate net profit
    net_profit = (r * min(q, demand)) + (s * max(0, q - demand)) - (c * q)
    
    profit.dist[j] = net_profit
  }
  
  # Calculate mean profit for the current quantity
  mean_profits[i] = mean(profit.dist)
  
  print('q is:')
  print(q)
  print('This was the mean profit simulated a thousand times for the above q:')
  print(mean_profits[i])
  print('---------------------------------------------------------------------')
}

# Plot results
plot(quantity, mean_profits, xlab = "Quantity (q)", ylab = "Mean Profit", main = "Mean Profit vs Quantity Purchased")
hist(profit.dist)


# Find the index of the maximum mean profit
max_mean_index <- which.max(mean_profits)

# Get the corresponding q value
optimal_q <- quantity[max_mean_index]

# Print the result
cat("The optimal q value for the highest mean profit is:", optimal_q, "\n")




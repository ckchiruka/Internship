#PMC Competition Curry Dataset


curry3 <- read.csv("C:/Users/ckashyap/Downloads/curry3.csv")
curryfirst = curry3[which(curry3$time > 24),] #scoring towards left hoop
currysecond = curry3[which(curry3$time < 24),] #scoring towards right hoop

firstshots = curryfirst[which(curryfirst$balllhoop < 1.5),]
firstcurryball = curryfirst[which(curryfirst$curryball < 1.5),]
secondshots = currysecond[which(currysecond$ballrhoop < 1.5),]
secondcurryball = currysecond[which(currysecond$curryball < 1.5),]

c = 0
last = 48
shots = list()
for (i in firstshots$time){
  current = i
  if(abs(current - last) > 0.001)
  {
    c = c+1
    startshot = current
    shots[c] = startshot
  }
  last = current
}

c = 0
last = 48
ball = list()
for (i in firstcurryball$time){
  current = i
  if(abs(current - last) > 0.001)
  {
    c = c+1
    startshot = last
    ball[c] = last
  }
  last = current
}

curryshots = numeric(0)
for(i in ball){
  for(j in shots)
    if((i - j) < 0.03 & (i-j) > 0)
      curryshots = c(curryshots, i)
}

c = 0
last = 48
shots2 = list()
for (i in secondshots$time){
  current = i
  if(abs(current - last) > 0.001)
  {
    c = c+1
    startshot = current
    shots2[c] = startshot
  }
  last = current
}

c = 0
last = 48
ball2 = list()
for (i in secondcurryball$time){
  current = i
  if(abs(current - last) > 0.001)
  {
    c = c+1
    startshot = last
    ball2[c] = last
  }
  last = current
}

for(i in ball2){
  for(j in shots2)
    if((i - j) < 0.03 & (i - j) > 0)
      curryshots = c(curryshots, i)
}

curryshots = unique(curryshots)

last = 48
remove = numeric(0)
for(i in curryshots){
  current = i
  if(last - current < 0.05)
    remove = c(remove, last)
  last = current
}
index = which(curry3$time %in% curryshots)



remove2 = function(index, curry3){
  getrid = numeric(0)
  for(i in index){
    c = 0
    if(curry3$time[i] > 24)
    {
      j = i
      while(curry3$balllhoop[j] > 1.5){
        slope = (curry3$balllhoop[j] - curry3$balllhoop[j+1])/(curry3$time[j] - curry3$time[j+1])
        j = j+1
        if(slope < 0)
        {
          c = c + 1
          if(c > 2)
            getrid = c(getrid, curry3$time[i])
        }
      }
    }
    if(curry3$time[i] < 24)
    {
      j = i
      while(curry3$ballrhoop[j] > 1.5){
        slope = (curry3$ballrhoop[j] - curry3$ballrhoop[j+1])/(curry3$time[j] - curry3$time[j+1])
        j = j+1
        if(slope < 0)
        {
          c = c + 1
          if(c > 2)
            getrid = c(getrid, curry3$time[i])
        }
      }
    }
  }
  return(unique(getrid))
}

getrid = remove2(index, curry3)

curryshots = curryshots[!curryshots %in% remove]
curryshots = curryshots[!curryshots %in% getrid]
currystart = curry3[which((curry3$time %in% curryshots)) + 20 , ]
currystop = curry3[which((curry3$time %in% curryshots)) - 7 , ]
finalcurry = data.frame(currystop$time, currystart$time)
write.csv(finalcurry, row.names=FALSE)


#Applied Linear Statistical Models Chapter 4 Projects
#4.26

CDI <- read.table("~/Previous Classes/STA 108/CDI.txt", quote="\"", comment.char="")

totalpop_physician = lm(V8~V5, data = CDI)

confint(totalpop_physician, level = (1 - .05/2)) 

#The joint confidence intervals supports what the investigator has suggested (B0 = -100,
#B1 = .0028)

W = sqrt(2*qf(.90, 2, 438))
B = qt(1 - .10/6, 438)

#Since Bonferroni (B) gives the tighter confidence limits, it's better to use it

newdata = data.frame(V5 = c(500, 1000, 5000))

predict(totalpop_physician, newdata, interval = "confidence", level = (1 - .10/3))

#These confidence intervals give us the range for B0 for X = 500, 1000, 5000 
#with family confidence 90%



#Applied Linear Statistical Models Chapter 1 Projects
#1.43

CDI <- read.table("~/Previous Classes/STA 108/CDI.txt", quote="\"", comment.char="")

totalpop_physician = lm(V8~V5, data = CDI)
totalpop_physician
plot(CDI$V5, CDI$V8, xlab = "Total Population", ylab = "Number of Physicians")
abline(totalpop_physician)
totalpopmse = sum(summary(totalpop_physician)$residuals^2)/(440-2)

hospitalbeds_physician = lm(V8~V9, data = CDI)
hospitalbeds_physician
plot(CDI$V9, CDI$V8, xlab = "Number of Hospital Beds", ylab = "Number of Physicians")
abline(hospitalbeds_physician)
hospitalbedsmse = sum(summary(hospitalbeds_physician)$residuals^2)/(440-2)

totincome_physician = lm(V8~V16, data = CDI)
totincome_physician
plot(CDI$V16, CDI$V8, xlab = "Total Income", ylab = "Number of Physicians")
abline(totincome_physician)
totincomemse = sum(summary(totincome_physician)$residuals^2)/(440-2)

#Hopital beds as a predictor variable leads to the lowest variability around the 
#regression line


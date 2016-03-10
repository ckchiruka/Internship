#Applied Linear Statistical Models Chapter 3 Projects
#3.24

X = c(5, 8, 11, 7, 13, 12, 12, 6)
Y = c(63, 67, 74, 64, 75, 69, 90, 60)
bloodpr = data.frame(X, Y)

bloodpr.lrm = lm(Y~X, data = bloodpr)
bloodpr.lrm

bloodpr.res = resid(bloodpr.lrm)
plot(bloodpr$X, bloodpr.res, ylab = "Residuals", xlab = "Age")
abline(0,0)

#There seems to be an outlier in the residuals

bloodpr = bloodpr[-c(7),]

bloodpr.lrm2 = lm(Y~X, data = bloodpr)
bloodpr.lrm2

bloodpr.res2 = resid(bloodpr.lrm2)
plot(bloodpr$X, bloodpr.res2, ylab = "Residuals", xlab = "Age")
abline(0,0)

#These new residuals seem much better with lower variance

age12 = data.frame(X = 12)

predict(bloodpr.lrm2, age12, interval = "predict", level = .99)

#Observation 7 was beyond our 99% confidence interval, which makes it an outlier
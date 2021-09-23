

#######
#### encolsing dir is working dir
#################  source("___go_example_JP.R")


library(gdata)

xdf <- read.xls("added1d_new_Influencerpaygap.xlsx")


head(xdf)



options(width=180)

f_dummy <- function(x, facname=NULL) {
    u.x <- sort( unique(x) )
    d <- length(u.x)
    mx.out <- matrix(0, length(x), d)
    for(i in 1:d) {
        mx.out[ , i] <- as.integer( u.x[i] == x )
    }
    colnames(mx.out) <- paste0(facname, u.x)
    return(mx.out)
}


########### experimental

x1 <- tolower(gsub("^\\s*|\\s*$|\n|\t", "", xdf[ , "INDUSTRY.FOCUS" ]))
lsx1 <- strsplit(x1, ",")
xxx <- lapply(lsx1, function(x) { return( gsub("^\\s*|\\s*$|\n|\t", "", x ) ) } )
x1tbl <- table(unlist(xxx))

mxOutDummy <- matrix(0, length(x1), length(x1tbl))
colnames(mxOutDummy) <- names(x1tbl)

for(ii in 1:length(x1)) {
    
    these_cats <- xxx[[ ii ]] ; these_cats
    
    mxOutDummy[ ii, these_cats ] <- 1
    
}
colnames(mxOutDummy) <- paste0("x3__", colnames(mxOutDummy))

###### important, see dummy assignment below




x1 <- tolower(gsub("^\\s*|\\s*$|\n|\t", "", xdf[ , "INDUSTRY.FOCUS" ]))
x1[ x1 %in% "n/a" ] <- NA


x2 <- tolower(gsub("^\\s*|\\s*$", "", xdf[ , "RACE" ]))
x2[ x2 %in% "n/a" ] <- NA



x3 <- tolower(gsub("^\\s*|\\s*$", "", xdf[ , "SEXUAL.ORIENTATION" ]))
x3[ x3 %in% "n/a" ] <- NA


###### numerical
x10 <- tolower(gsub("^\\s*|\\s*$|%", "", xdf[ , "ENGAGEMENT.RATE" ]))
x10[ x10 %in% "n/a" ] <- NA
x10 <- as.numeric(x10)

data.frame(x10, xdf[ , "ENGAGEMENT.RATE" ])

#x10 <- log(x10 + 1)



x11 <- tolower(gsub("^\\s*|\\s*$|%", "", xdf[ , "FOLLOWER.COUNT_1" ]))
x11[ x11 %in% "n/a" ] <- NA
x11 <- as.numeric(x11)



x12 <- tolower(gsub("^\\s*|\\s*$|%", "", xdf[ , "FOLLOWER.COUNT_2" ]))
x12[ x12 %in% "n/a" ] <- NA
x12 <- as.numeric(x12)



x13 <- tolower(gsub("^\\s*|\\s*$|%", "", xdf[ , "PAGE.VIEWS" ]))
x13[ x13 %in% "n/a" ] <- NA
x13 <- as.numeric(x13)


yy <- tolower(gsub("^\\s*|\\s*$|%", "", xdf[ , "FEE.dollar." ]))
yy[ yy %in% "n/a" ] <- NA
yy <- as.numeric(yy)

############ transform FEE
yy <- log( yy + 1 )


######### method 1

## mx1 <- f_dummy(x=x1, facname="x1__")
mx1 <- mxOutDummy ### from above


mx2 <- f_dummy(x=x2, facname="x2__")
mx3 <- f_dummy(x=x3, facname="x3__")




######### convert NA to cat

#x10 <- log(x10+1)
#x11 <- log(x11+1)
#x12 <- log(x12+1)
#x13 <- log(x13+1)



mxX <- cbind(mx1, mx2, mx3, x10, x11, x12, x13)
mxX


#mxX <- cbind(x10, x11, x12, x13)
#mxX





############################################## NOW FIT
######################################### make XY

n <- nrow(mxX)

mxXY <- cbind("y"=yy, "int"=rep(1, n), mxX)
mxXY                                     ###### this is the response and desgin matrix all together!



xnames <- c("int", colnames(mxX)) ; xnames
ynames <- "y"



naXY <- as.integer(!is.na(mxXY))
dim(naXY) <- dim(mxXY)

xymeans <- apply(mxXY, 2, mean, na.rm=TRUE) ; xymeans
xysds <- sqrt(apply(mxXY, 2, var, na.rm=TRUE) * (n-1) / n) ; xysds

cbind(xymeans, xysds)

xymeans[ "int" ] <- 0
xysds[ "int" ] <- 1

############# run together
mxXYstnd <- t( (t(mxXY) - xymeans) / xysds )
mxXYstnd[ is.na(mxXYstnd) ] <- 0
############# run together



naXYXY <- crossprod(naXY) ; naXYXY
naXYXY <- naXYXY + 1

Lxyxy <- crossprod(mxXYstnd) / naXYXY #### very much like correlation mx

xreg <- 1/10

Lxx <- Lxyxy[ xnames, xnames ]
Lxy <- Lxyxy[ xnames, ynames, drop=FALSE ]

bbhat <- solve( Lxx + diag(xreg, ncol(Lxx)) ) %*% Lxy

yyhat <- mxXYstnd[ , xnames ] %*% bbhat

plot(yyhat, yy)

cor(yyhat, yy, use="complete.obs")


####################### as a function

f_solveXY <- function(mxXY, xreg, xnames, ynames) {
    
    #mxXY <- cbind("y"=yy[ ,1], "int"=rep(1, n), mxX)
    #mxXY

    naXY <- as.integer(!is.na(mxXY))
    dim(naXY) <- dim(mxXY)
    
    n <- nrow(mxXY)

    xymeans <- apply(mxXY, 2, mean, na.rm=TRUE) ; xymeans
    xysds <- sqrt(apply(mxXY, 2, var, na.rm=TRUE) * (n-1) / n) ; xysds

    xymeans[ "int" ] <- 0
    xysds[ "int" ] <- 1

    ############# run together
    mxXYstnd <- t( (t(mxXY) - xymeans) / xysds )
    mxXYstnd[ is.na(mxXYstnd) ] <- 0
    ############# run together

    naXYXY <- crossprod(naXY)
    naXYXY <- naXYXY + 1

    Lxyxy <- crossprod(mxXYstnd) / naXYXY ##### the 'average' product

    Lxx <- Lxyxy[ xnames, xnames, drop=FALSE ]
    Lxy <- Lxyxy[ xnames, ynames, drop=FALSE ]

    bbhat <- solve( Lxx + diag(xreg, ncol(Lxx)) ) %*% Lxy

    yyhat <- mxXYstnd[ , xnames, drop=FALSE ] %*% bbhat
    
    ls_out <- list("yhat"=yyhat, "bhat"=bbhat, "xymeans"=xymeans, "xysds"=xysds )
    return(ls_out)
    
}




xyobj <- f_solveXY(mxXY=mxXY, xreg=1/100, xnames, ynames)



######################## find best reg



xreg_vec <- seq(1/1000000, 1/5, length.out=300)

xreg_vec <- seq(1/1000000, 100, length.out=100)


xrmse_out <- rep(NA, length(xreg_vec))

iireg <- 50

for(iireg in 1:length(xreg_vec)) {
    
    xthis_reg <- xreg_vec[iireg]
    
    ylo_hat <- rep(NA, n)
    iilo <- 1
    for(iilo in 1:n) {
        
        xyobj <- f_solveXY(mxXY=mxXY[ -iilo, , drop=FALSE ], xreg=xthis_reg, xnames=xnames, ynames=ynames)
        
        xthis_mxxy_stnd <- t( ( t(mxXY[ iilo, xnames, drop=FALSE ]) - xyobj[[ "xymeans" ]][ xnames ] ) / xyobj[[ "xysds" ]][ xnames ] )
        xthis_mxxy_stnd[ is.na(xthis_mxxy_stnd) ] <- 0
        
        yhat_stnd <- xthis_mxxy_stnd %*% xyobj[[ "bhat" ]]
        
        ###### return yhat to original scale
        ylo_hat[iilo] <- yhat_stnd * xyobj[[ "xysds" ]][ ynames ] + xyobj[[ "xymeans" ]][ ynames ]
        
    }
    
    xrmse_out[iireg] <- sqrt( mean( ( yy - ylo_hat )^2, na.rm=TRUE ) ) #### RMSE
    cat(iireg, xthis_reg, "\n")
}


plot(xreg_vec, xrmse_out, type="l")


xreg_vec[ which.min(xrmse_out) ]



par(mfrow=c(1,2))
plot(xreg_vec, xrmse_out, type="l")
hist(yy)

yyvar <- var(yy, na.rm=TRUE) * (n-1) / n
yyvar

cat("R2:",
1 - min(xrmse_out)^2 / yyvar,
"\n")



#######################

## break() ;

xour_best_reg <- xreg_vec[ which.min(xrmse_out) ] ; xour_best_reg

mxXY0 <- mxXY[ 2, , drop=FALSE ]

mxXY0[ , "y" ] <- NA
#mxXY0[ , "x3__beauty" ] <- 1

mxXYnew_with0 <- rbind(mxXY0, mxXY)

xyobj <- f_solveXY(mxXY=mxXYnew_with0, xreg=xour_best_reg, xnames=xnames, ynames=ynames)

y0hat_stnd <- xyobj[[ "yhat" ]][ , "y" ][ c(1, 3) ]

y0hat <- y0hat_stnd * xyobj[[ "xysds" ]][ ynames ] + xyobj[[ "xymeans" ]][ ynames ] ; y0hat


yohat_fee <- exp(y0hat) - 1

yohat_fee




#####################
obs1 <-
cbind(
"y"=NA,
"int"=1,
"x3__art"=0,
"x3__beauty"=1,
"x3__comedy"=0,
"x3__education"=0,
"x3__food"=0,
"x3__hair"=0,
"x3__health"=0,
"x3__journal"=0,
"x3__lifestyle"=0,
"x3__n/a"=0,
"x3__parenting"=0,
"x3__pet products"=0,
"x3__travel"=0,
"x2__asian"=0,
"x2__black"=0,
"x2__hispanic"=0,
"x2__mixed"=1,
"x2__white"=0,
"x3__lgbtq"=0,
"x3__straight"=1,
"x10"=11,
"x11"=7200,
"x12"=3600,
"x13"=1860
)




#####################
obs2 <-
cbind(
"y"=NA,
"int"=1,
"x3__art"=0,
"x3__beauty"=1,
"x3__comedy"=0,
"x3__education"=0,
"x3__food"=0,
"x3__hair"=0,
"x3__health"=0,
"x3__journal"=0,
"x3__lifestyle"=0,
"x3__n/a"=0,
"x3__parenting"=0,
"x3__pet products"=0,
"x3__travel"=0,
"x2__asian"=0,
"x2__black"=0,
"x2__hispanic"=0,
"x2__mixed"=1,
"x2__white"=0,
"x3__lgbtq"=1, #####
"x3__straight"=0,
"x10"=11,
"x11"=7200,
"x12"=3600,
"x13"=1860
)




mxXYnew_with0 <- rbind(obs1, obs2, mxXY)

xyobj <- f_solveXY(mxXY=mxXYnew_with0, xreg=xour_best_reg, xnames=xnames, ynames=ynames)

y0hat_stnd <- xyobj[[ "yhat" ]][ , "y" ][ c(1, 2) ]

y0hat <- y0hat_stnd * xyobj[[ "xysds" ]][ ynames ] + xyobj[[ "xymeans" ]][ ynames ] ; y0hat


yohat_fee <- exp(y0hat) - 1

yohat_fee



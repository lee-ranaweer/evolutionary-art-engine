```
sum = 0.0
for(x = 0; x < width;++x){
   for(y = 0; y < height; ++y){
      difference = (A[x,y] - B[x,y])
      sum = sum + difference*difference
   }
}
mse = sum /(width*height)
printf("The mean square error is %f\n",mse)
```

Similar = less MSE
Different = more MSE
Must be same width and height
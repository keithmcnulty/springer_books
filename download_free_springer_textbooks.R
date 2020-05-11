if (!("openxlsx" %in% installed.packages())) {
  install.packages("openxlsx")
}

library(openxlsx)

wb <- openxlsx::read.xlsx("Free+English+textbooks.xlsx")

convert_to_dd <- function (url) {
  x <- gsub("http://doi.org/", "", url)
  paste0("https://link.springer.com/content/pdf/", x, ".pdf")
}

if (!dir.exists("books")) {
  dir.create("books")
}

for (i in 1:nrow(wb)) {
  download.file(convert_to_dd(wb$DOI.URL[i]), destfile = paste0("books/", wb$Book.Title[i], ".pdf"))  
}


import scala.io.Source
import java.io.{File, PrintWriter}

object Question6Scala {
	def main(args: Array[String]) {

		println("Question 6 Scala: \n")
		
		// Read Text
		val text = Source.fromFile("file.txt").mkString

		// Print from Text
		println("Scala: " + text)
		
		// Write to CSV
		val writer = new PrintWriter(new File("scala.csv"))
		var csvData = new StringBuffer("")
		csvData.append(text)
            	writer.write(csvData.toString())
		writer.close()
		
		println("CSV created\n")	
	}
}

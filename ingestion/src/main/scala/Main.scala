import zio._
import zio.http._
import service.ScrapperServiceHandler

object Main extends ZIOAppDefault {

  override def run: ZIO[Any, Any, Any] = {
    for {
      _ <- ZIO.logInfo("🚀 Starting the Scala Ingestion Gateway...")
      
      // Initialize the gRPC Service Layer
      _ <- ZIO.logInfo("🌍 Scala gRPC Server binding to port 50051...")
      
      // In a real ZIO-gRPC setup, we would use Server.start or similar
      // For now, we simulate the long-running server process
      _ <- ZIO.never
    } yield ()
  }
}
//Nome do nosso pacote //                
//Classes necessárias para uso de Banco de dados //
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
//Início da classe de conexão//

public class ConexaoMySQL {
    
    private static ConexaoMySQL instance = null;         
    private Connection connection = null;
    public static String status ;
    
    //Método Construtor da Classe//
    public ConexaoMySQL() {
    }
    //Método de Conexão//
    public static java.sql.Connection getConexaoMySQL() {  
        Connection connection = null;          //atributo do tipo Connection
        try {
            // Carregando o JDBC Driver padrão
            Class.forName("com.mysql.cj.jdbc.Driver");
            String mydatabase ="crud";        //nome do seu banco de dados           
            String username = "admin";        //nome de um usuário de seu BD                  
            String password = "minich25";      //sua senha de acesso      
            String url = "jdbc:mysql://bancotdt.cvhdbqmicdap.us-east-1.rds.amazonaws.com:3306/" + mydatabase + "?user=" + username + "&password=" + password;                  
            connection = DriverManager.getConnection(url);

            //Testa sua conexão//  
            if (connection != null) {
                status = ("STATUS--->Conectado com sucesso!");
            } else {
                status = ("STATUS--->Não foi possivel realizar conexão");
            }
            return connection;   
        } catch (SQLException e) {
            //Não conseguindo se conectar ao banco
            System.out.println("Nao foi possivel conectar ao Banco de Dados." + e);
            return connection;
        } catch (ClassNotFoundException e) {
			e.printStackTrace();
            return connection;
		} 
    }   
    //Método que retorna o status da sua conexão//   
    public static String statusConection() {
        return status;        
    }   
    //Método que fecha sua conexão//    
    public static boolean FecharConexao() {       
        try {           
            ConexaoMySQL.getConexaoMySQL().close();           
            return true;           
        } catch (SQLException e) {           
            return false;          
        }        
    }
   //Método que reinicia sua conexão//
    public static java.sql.Connection ReiniciarConexao() {       
        FecharConexao();        
        return ConexaoMySQL.getConexaoMySQL();        
    }
}
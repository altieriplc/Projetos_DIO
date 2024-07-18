import sqlalchemy
from sqlalchemy.orm import declarative_base, Session #Session: É uma classe que encapsula uma "sessão" de trabalho com o banco de dados. Ela mantém controle das operações e transações realizadas no banco de dados. As instâncias de Session são utilizadas para enviar comandos SQL e receber resultados, além de gerenciar o ciclo de vida das transações.
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, func, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import select

# import sqlalchemy: Importa o SQLAlchemy, que é uma biblioteca para trabalhar com bancos de dados relacionais em Python.
# SQLAlchemy segue uma abordagem modular. Isso significa que ele não carrega automaticamente todos os seus componentes diretamente no namespace principal quando você importa sqlalchemy em si, por isso é necessário importar especificamente cada um.
# Isso ajuda a manter o código mais claro e evita poluir o namespace com funcionalidades que você pode não precisar utilizar.

Base = declarative_base()  # Base = estrutura modelo que vai ser utilizada para criar as classes da aplicação
# 
# declarative_base: É uma função que retorna uma classe base especial do SQLAlchemy chamada DeclarativeMeta. Esta classe base é utilizada para criar classes de mapeamento de objetos (ORM) que representam tabelas no banco de dados. Ela permite definir estruturas de dados Python que são automaticamente mapeadas para tabelas no banco de dados, facilitando a interação entre objetos Python e dados persistidos em um banco de dados relacional.


class User(Base):  # classe user está herdando as caracteristica de Base
    __tablename__ = 'user_account'  # __tablename__ não é método, mas uma convensão para se nomear tabelas
    # definir atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )  # 'back_populates' estabelece um relacionamento bidirecional entre classes em SQLAlchemy.
        #delete orphan define a relação do obejto filho com o objeto pai
    # Define o atributo na classe atual que acessa objetos da classe relacionada,
    # garantindo que ambos os lados do relacionamento estejam sempre sincronizados.
    # Exemplo: 'user' em Address acessa objetos User, 'address' em User acessa objetos Address.
    def __repr__(self):  # este método retorna uma string que representa o objeto.
        return f'User (id={self.id}, name={self.name}, fullname={self.fullname})'


class Address(Base):
    __tablename__ = "user_address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship('User', back_populates='address')

    def __repr__(self):
        return f'Address (id={self.id}, email_address={self.email_address})'

print('Imprime o nome das tabelas')
print(User.__tablename__)
print(Address.__tablename__)



# ------ https://erd.dbdesigner.net/designer/schema/1719837803-aula_dio ------ #
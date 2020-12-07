from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, \
    BOOLEAN, TIME, Text, SMALLINT, ForeignKey, DATETIME, TEXT

engine = create_engine("mysql+pymysql://root:Rootpass12345@localhost/testflask", echo=True)
meta = MetaData()

Message = Table(
   'message', meta,
   Column('id', Integer, primary_key=True),
   Column('text', String(255), nullable=False),
   #Column('text', Integer, primary_key=True),
 )

Tag = Table(
   'tag', meta,
   Column('id', Integer, primary_key=True),
   Column('text', String(32), nullable=False),
   #Column('message_id', Integer, ForeignKey('Message.id'), nullable=False),

 )
Post = Table(
    'post', meta,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('title', String(100), nullable=False),
    Column('date_posted', DATETIME, nullable=False),
    Column('content', TEXT, nullable=False),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
)

User = Table(
    'user', meta,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('username', String(80)),
    Column('email', String(120)),
    Column('password', String(80)),
    Column('image_file', String(20), nullable=False),
    # Column(primary_key=True, 'id'),
)

meta.create_all(engine)
conn = engine.connect()
# Message.drop(engine)
# Tag.drop(engine)
# User.drop(engine)

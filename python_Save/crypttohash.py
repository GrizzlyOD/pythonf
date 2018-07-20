from cryptography.fernet import Fernet
import base64
key = Fernet.generate_key()
# base64.urlsafe_b64encode(os.urandom(32))
# os.urandom():Return a bytes object containing random bytes suitable for cryptographic use
# 产生了一个32位随机数，并用base64编码
f = Fernet(key)
#        if backend is None:
#             backend = default_backend()
#
#         key = base64.urlsafe_b64decode(key)
#         if len(key) != 32:
#             raise ValueError(
#                 "Fernet key must be 32 url-safe base64-encoded bytes."
#             )
#
#         self._signing_key = key[:16]
#         self._encryption_key = key[16:]
#         self._backend = backend
# 生成32位密钥后，前16位用来计算hmac，后16位用来加解密
token = f.encrypt(b'u r sb')
#    def encrypt(self, data):
#         current_time = int(time.time())                               生成当前时间
#         iv = os.urandom(16)                                           随机生成16为vi用于cbc
#         return self._encrypt_from_parts(data, current_time, iv)       传到下级函数
#
#     def _encrypt_from_parts(self, data, current_time, iv):
#         if not isinstance(data, bytes):
#             raise TypeError("data must be bytes.")                    数据必须是字符类型
#
#         padder = padding.PKCS7(algorithms.AES.block_size).padder()    填充标准器为pkcs7（aes数据块大小128）
#         padded_data = padder.update(data) + padder.finalize()         把加密数据用填充器补齐
#         encryptor = Cipher(
#             algorithms.AES(self._encryption_key), modes.CBC(iv), self._backend
#         ).encryptor()                                                 设置加密器，用aes方式加密，上面生成的key，iv，backend
#         ciphertext = encryptor.update(padded_data) + encryptor.finalize()
#
#         basic_parts = (
#             b"\x80" + struct.pack(">Q", current_time) + iv + ciphertext
#                                                       把current_time、iv、ciphertext三者合并得到一个basic_parts
#         )
#
#         h = HMAC(self._signing_key, hashes.SHA256(), backend=self._backend)
#         h.update(basic_parts)                计算basic_parts的hmac值
#         hmac = h.finalize()
#         return base64.urlsafe_b64encode(basic_parts + hmac)
#把basic_parts + hmac 做base64计算后返回，这就是我们最终得到的加密数据，里面包含了时间戳、iv、密文、hmac
print(token)
a = f.decrypt(token)
#解码相反,缺省ttl=none（最大存在时间）最大时钟偏差为60
# 1. 得到current_time
# 2. base64解码token，得到包含时间戳、iv、密文、hmac的data
# 3. 根据时间戳和ttl，判断密钥是否已经失效
# 4. 计算hmac，并于之前的hmac进行验证，判断密钥有效性
# 5. 获取iv，和密文，并通过密钥解密，得到经过pad的明文
# 6. 通过PKCS7进行unpaid操作，得到去掉补齐的明文
# 7. 返回最终结果
print(a)
print(key)
#Token是服务端生成的一串字符串，
# 以作客户端进行请求的一个令牌，
# 当第一次登录后，
# 服务器生成一个Token便将此Token返回给客户端，
# 以后客户端只需带上这个Token前来请求数据即可，
# 无需再次带上用户名和密码。
#http://blog.csdn.net/zglwy/article/details/53512065
print(base64.urlsafe_b64decode(token))
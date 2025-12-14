/**
 * 图片URL处理工具函数
 * 将数据库中的图片路径转换为完整的URL
 */
export function getImageUrl(imagePath) {
  if (!imagePath) return ''
  
  // 如果是完整URL（http/https开头），直接返回
  if (imagePath.startsWith('http://') || imagePath.startsWith('https://')) {
    return imagePath
  }
  
  // 如果是多张图片，取第一张
  const firstImage = imagePath.split(',')[0].trim()
  
  // 如果已经是 /upload/ 开头的路径，拼接完整URL
  if (firstImage.startsWith('/upload/')) {
    return `http://localhost:8080/foodie${firstImage}`
  }
  
  // 如果是相对路径（没有/upload/前缀），也拼接完整URL
  return `http://localhost:8080/foodie/upload/${firstImage}`
}



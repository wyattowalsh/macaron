import React from 'react';
import { motion } from 'framer-motion';

const ToolCard = ({ tool }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className="p-6 border rounded-lg shadow-sm hover:shadow-lg transition-shadow bg-white relative overflow-hidden"
    >
      <div
        className="absolute inset-0 bg-cover bg-center opacity-20"
        style={{ backgroundImage: `url(${tool.image})`, transform: 'scale(1.2)' }}
      ></div>
      <div className="relative z-10">
        <h3 className="text-2xl font-semibold mb-2">
          <a href={tool.link} className="text-blue-600 hover:underline">
            {tool.name}
          </a>
        </h3>
        <p className="text-gray-700 mb-4">{tool.description}</p>
        <div className="flex flex-wrap gap-2">
          {tool.tags.map((tag) => (
            <span
              key={tag}
              className="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm"
            >
              {tag}
            </span>
          ))}
        </div>
      </div>
    </motion.div>
  );
};

export default ToolCard;

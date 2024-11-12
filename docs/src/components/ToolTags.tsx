import { motion } from 'framer-motion';
import React from 'react';
import { useLocation } from '@docusaurus/router';
import tools from '../constants/toolsData';
import { Badge } from './ui/badge';

const ToolTags: React.FC = () => {
  const location = useLocation();
  const toolName = location.pathname.split('/').pop()?.toLowerCase();

  const tool = tools.find((t) => t.name.toLowerCase() === toolName);

  if (!tool) {
    return null;
  }

  return (
    <div className="flex flex-wrap gap-2 mb-4">
      {tool.tags.map((tag) => (
        <motion.div
          key={tag}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className="cursor-pointer"
        >
          <Badge variant="outline" className="hover:bg-primary hover:text-white">
            {tag}
          </Badge>
        </motion.div>
      ))}
    </div>
  );
};

export default ToolTags;
